"""TODO: To implement."""


from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Callable,
    Coroutine,
    Dict,
    Generator,
    Generic,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)

from peewee import (
    SQL,
    DeferredForeignKey,
    Expression,
    Field,
    ForeignKeyAccessor,
    ForeignKeyField,
    Model,
    ModelAlias,
    ModelBase,
    ModelCompoundSelectQuery,
    ModelDelete,
    ModelInsert,
    ModelRaw,
    ModelSelect,
    ModelUpdate,
    Table,
)

from .types import TVAIOModel

if TYPE_CHECKING:
    from typing_extensions import Self  # py310,py39,py38,py37

    from .manager import Manager


class AIOForeignKeyAccessor(ForeignKeyAccessor):
    async def get_rel_instance(self, instance: AIOModel) -> Optional[AIOModel]:
        # Get from cache
        name = self.name
        if name in instance.__rel__:
            return instance.__rel__[name]

        value = instance.__data__.get(name)

        # Lazy load
        field = self.field
        if field.lazy_load:
            if value is not None:
                obj = await self.rel_model.get(self.field.rel_field == value)
                instance.__rel__[self.name] = obj
                return obj

            if not field.null:
                raise self.rel_model.DoesNotExist

        return value


class AIOForeignKeyField(ForeignKeyField):
    accessor_class = AIOForeignKeyAccessor


class AIODeferredForeignKey(DeferredForeignKey):
    def set_model(self, rel_model: Type[Model]):
        field = AIOForeignKeyField(rel_model, _deferred=True, **self.field_kwargs)
        self.model._meta.add_field(self.name, field)


class AIOModelBase(ModelBase):
    inheritable = ModelBase.inheritable & {"manager"}

    def __new__(cls, name, bases, attrs):
        # Replace fields to AIO fields
        for attr_name, attr in attrs.items():
            if not isinstance(attr, Field):
                continue

            if isinstance(attr, ForeignKeyField) and not isinstance(
                attr,
                AIOForeignKeyField,
            ):
                attrs[attr_name] = AIOForeignKeyField(
                    attr.rel_model,
                    field=attr.rel_field,
                    backref=attr.declared_backref,
                    on_delete=attr.on_delete,
                    on_update=attr.on_update,
                    deferrable=attr.deferrable,
                    _deferred=attr.deferred,
                    object_id_name=attr.object_id_name,
                    lazy_load=attr.lazy_load,
                    constraint_name=attr.constraint_name,
                    null=attr.null,
                    index=attr.index,
                    unique=attr.unique,
                    default=attr.default,
                    primary_key=attr.primary_key,
                    constraints=attr.constraints,
                    sequence=attr.sequence,
                    collation=attr.collation,
                    unindexed=attr.unindexed,
                    choices=attr.choices,
                    help_text=attr.help_text,
                    verbose_name=attr.verbose_name,
                    index_type=attr.index_type,
                    _hidden=attr._hidden,
                )

            elif isinstance(attr, DeferredForeignKey) and not isinstance(
                attr,
                AIODeferredForeignKey,
            ):
                attrs[attr_name] = AIODeferredForeignKey(
                    attr.rel_model_name,
                    **attr.field_kwargs,
                )
                DeferredForeignKey._unresolved.discard(attr)

        cls = super(AIOModelBase, cls).__new__(cls, name, bases, attrs)
        meta = cls._meta
        if getattr(cls, "_manager", None) and not meta.database:
            meta.database = cls._manager.pw_database

        return cls


class AIOModel(Model, metaclass=AIOModelBase):
    _manager: Manager

    # Class methods
    # -------------

    @classmethod
    async def create_table(cls, *, safe=True, **kwargs):
        return await cls._manager.create_tables(cls, safe=safe, **kwargs)

    @classmethod
    async def drop_table(cls, *, safe=True, **kwargs):
        return await cls._manager.drop_tables(cls, safe=safe, **kwargs)

    @classmethod
    async def get_or_none(
        cls: Type[TVAIOModel],
        *args: Expression,
        **kwargs,
    ) -> Optional[TVAIOModel]:
        return await cls._manager.get_or_none(cls, *args, **kwargs)

    @classmethod
    async def get(cls: Type[TVAIOModel], *args: Expression, **kwargs) -> TVAIOModel:
        return await cls._manager.get(cls, *args, **kwargs)

    @classmethod
    async def get_by_id(cls: Type[TVAIOModel], pk) -> TVAIOModel:
        return await cls._manager.get_by_id(cls, pk)

    @classmethod
    async def set_by_id(cls, key, value):
        return await cls._manager.set_by_id(cls, key, value)

    @classmethod
    async def delete_by_id(cls, pk):
        return await cls._manager.delete_by_id(cls, pk)

    @classmethod
    async def get_or_create(
        cls: Type[TVAIOModel],
        defaults: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Tuple[TVAIOModel, bool]:
        async with cls._manager.transaction():
            try:
                return (await cls.get(**kwargs), False)
            except cls.DoesNotExist:
                return (await cls.create(**dict(defaults or {}, **kwargs)), True)

    @classmethod
    async def create(cls: Type[TVAIOModel], **kwargs) -> TVAIOModel:
        inst = cls(**kwargs)
        return await inst.save(force_insert=True)

    @classmethod
    async def bulk_create(cls, **_):
        # TODO: To implement
        raise NotImplementedError("AIOModel doesnt support `bulk_create`")

    @classmethod
    async def bulk_update(cls, **_):
        # TODO: To implement
        raise NotImplementedError("AIOModel doesnt support `bulk_update`")

    # Queryset methods
    # ----------------

    @classmethod
    def select(
        cls: Type[TVAIOModel],
        *select: Union[Field, Model, Table, ModelAlias],
    ) -> AIOModelSelect[TVAIOModel]:
        return AIOModelSelect(
            cls,
            select or cls._meta.sorted_fields,
            is_default=not select,
        )

    @classmethod
    def update(
        cls: Type[TVAIOModel],
        __data=None,
        **update,
    ) -> AIOModelUpdate[TVAIOModel]:
        return AIOModelUpdate(cls, cls._normalize_data(__data, update))

    @classmethod
    def insert(
        cls: Type[TVAIOModel],
        __data=None,
        **insert,
    ) -> AIOModelInsert[TVAIOModel]:
        return AIOModelInsert(cls, cls._normalize_data(__data, insert))

    @classmethod
    def insert_many(
        cls: Type[TVAIOModel],
        rows: Iterable,
        fields=None,
    ) -> AIOModelInsert[TVAIOModel]:
        if not rows:
            raise AIOModelInsert.DefaultValuesException("Error: no rows to insert.")

        rows = [row.__data__ if isinstance(row, Model) else row for row in rows]
        return AIOModelInsert(cls, insert=rows, columns=fields)

    @classmethod
    def insert_from(
        cls: Type[TVAIOModel],
        query: ModelSelect,
        fields,
    ) -> AIOModelInsert[TVAIOModel]:
        columns = [getattr(cls, field) if isinstance(field, str) else field for field in fields]
        return AIOModelInsert(cls, insert=query, columns=columns)

    @classmethod
    def raw(cls: Type[TVAIOModel], sql, *params) -> AIOModelRaw[TVAIOModel]:
        return AIOModelRaw(cls, sql, params)

    @classmethod
    def delete(cls: Type[TVAIOModel]) -> AIOModelDelete[TVAIOModel]:
        return AIOModelDelete(cls)

    # Instance methods
    # ----------------

    async def save(self, **kwargs) -> Self:
        return await self._manager.save(self, **kwargs)

    async def delete_instance(self, **kwargs):
        return await self._manager.delete_instance(self, **kwargs)

    # Support await syntax
    # --------------------

    def __await__(self):
        return self.__anext__().__await__()

    async def __anext__(self):
        return self


class AIOQuery(Generic[TVAIOModel]):
    model: Type[TVAIOModel]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.manager = self.model._manager

    def __await__(self) -> Generator[Any, None, List[TVAIOModel]]:
        return self.manager.run(self).__await__()


class BaseModelSelect(AIOQuery[TVAIOModel]):
    def union_all(self, rhs):
        return AIOModelCompoundSelectQuery(self.model, self, "UNION ALL", rhs)

    __add__ = union_all

    def union(self, rhs):
        return AIOModelCompoundSelectQuery(self.model, self, "UNION", rhs)

    __or__ = union

    def intersect(self, rhs):
        return AIOModelCompoundSelectQuery(self.model, self, "INTERSECT", rhs)

    __and__ = intersect

    def except_(self, rhs):
        return AIOModelCompoundSelectQuery(self.model, self, "EXCEPT", rhs)

    __sub__ = except_

    async def prefetch(self, *subqueries) -> List[TVAIOModel]:
        return await self.manager.prefetch(self, *subqueries)


class AIOModelSelect(BaseModelSelect[TVAIOModel], ModelSelect):
    _limit: int

    def __aiter__(self) -> AsyncGenerator[TVAIOModel, None]:
        return self.manager.run(self).__aiter__()

    def __getitem__(
        self,
        value,
    ) -> Union[AIOModelSelect[TVAIOModel], Coroutine[Any, Any, TVAIOModel]]:
        limit, offset = 1, value
        if isinstance(value, slice):
            limit, offset = value.stop - value.start, value.start

        query = self.limit(limit).offset(offset)
        if limit == 1:
            return query.get()
        return query

    async def peek(self, n=1) -> TVAIOModel:
        if n == 1:
            return await self.manager.fetchone(self)
        return await self.manager.fetchmany(n, self)

    def first(self, n=1) -> Coroutine[Any, Any, Optional[TVAIOModel]]:
        query = self
        if self._limit != n:
            query = self.limit(n)
        return query.peek(n)

    async def scalar(self, *, as_tuple=False, as_dict=False):
        if as_dict:
            return await self.dicts().peek()
        row = await self.tuples().peek()
        return row[0] if row and not as_tuple else row

    async def scalars(self) -> List[Any]:
        return [row[0] for row in await self.tuples()]

    async def count(self) -> int:
        return await self.manager.count(self)

    async def exists(self) -> bool:
        clone: AIOModelSelect = self.columns(SQL("1"))
        clone._limit = 1
        clone._offset = None
        return bool(await clone.scalar())

    async def get(self, **filters) -> TVAIOModel:
        qs = self
        if filters:
            qs = self.filter(**filters)

        res = await qs.first()
        if res is None:
            sql, params = qs.sql()
            raise self.model.DoesNotExist(
                "%s matching query does not exist:\n SQL: %s\n Params: %s"
                % (self.model, sql, params)
            )
        return res

    # Type helpers
    with_cte: Callable[..., AIOModelSelect[TVAIOModel]]
    where: Callable[..., AIOModelSelect[TVAIOModel]]
    orwhere: Callable[..., AIOModelSelect[TVAIOModel]]
    order_by: Callable[..., AIOModelSelect[TVAIOModel]]
    order_by_extend: Callable[..., AIOModelSelect[TVAIOModel]]
    limit: Callable[[Union[int, None]], AIOModelSelect[TVAIOModel]]
    offset: Callable[[int], AIOModelSelect[TVAIOModel]]
    paginate: Callable[..., AIOModelSelect[TVAIOModel]]

    columns: Callable[..., AIOModelSelect[TVAIOModel]]
    select_extend: Callable[..., AIOModelSelect[TVAIOModel]]
    from_: Callable[..., AIOModelSelect[TVAIOModel]]
    join: Callable[..., AIOModelSelect[TVAIOModel]]
    join_from: Callable[..., AIOModelSelect[TVAIOModel]]
    group_by: Callable[..., AIOModelSelect[TVAIOModel]]
    having: Callable[..., AIOModelSelect[TVAIOModel]]
    distinct: Callable[..., AIOModelSelect[TVAIOModel]]
    window: Callable[..., AIOModelSelect[TVAIOModel]]
    for_update: Callable[..., AIOModelSelect[TVAIOModel]]
    lateral: Callable[..., AIOModelSelect[TVAIOModel]]


class AIOModelCompoundSelectQuery(
    BaseModelSelect[TVAIOModel],
    ModelCompoundSelectQuery,
):
    pass


class AIOModelUpdate(AIOQuery[TVAIOModel], ModelUpdate):
    pass


class AIOModelInsert(AIOQuery[TVAIOModel], ModelInsert):
    pass


class AIOModelDelete(AIOQuery[TVAIOModel], ModelDelete):
    pass


class AIOModelRaw(AIOQuery[TVAIOModel], ModelRaw):
    pass
