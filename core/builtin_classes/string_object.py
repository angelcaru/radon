from core.builtin_classes.base_classes import BuiltInObject, check, method, operator
from core.builtin_funcs import args
from core.datatypes import Array, Boolean, Null, Number, String, Value
from core.errors import RTError
from core.parser import Context, RTResult


class StringObject(BuiltInObject):
    """Buili-in String manipulation object."""

    @operator("__constructor__")
    @check([String], [String("")])
    def constructor(self, string: String) -> RTResult[Value]:
        self.value: str = string.value
        return RTResult[Value]().success(Null.null())

    @operator("__add__")
    @check([String])
    def add(self, other: String) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(String(self.value + other.value))

    def __string_display__(self) -> str:
        """This method helps __repr__ to display as we want."""
        return self.value

    def __len__(self) -> int:
        """Return the length of string."""
        return len(self.value)

    @args([])
    @method
    def upper(self, _ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(String(self.value.upper()))

    @args([])
    @method
    def lower(self, _ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(String(self.value.lower()))

    @args([])
    @method
    def title(self, _ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(String(self.value.title()))

    @args([])
    @method
    def capitalize(self, _ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(String(self.value.capitalize()))

    @args([])
    @method
    def swapcase(self, _ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(String(self.value.swapcase()))

    @args([])
    @method
    def length(self, _ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        return res.success(Number(len(self.value)))

    @args(["string"], [String("")])
    @method
    def count(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot count a non-string", string.context))
        if len(string.value) == 0:
            return res.failure(
                RTError(string.pos_start, string.pos_end, "Cannot count an empty string", string.context)
            )
        return res.success(Number(self.value.count(string.value)))

    @args(["string", "value"], [String(""), String("")])
    @method
    def replace(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot replace a non-string", string.context))
        value = ctx.symbol_table.get("value")
        assert value is not None
        if not isinstance(value, String):
            return res.failure(RTError(value.pos_start, value.pos_end, "Cannot replace a non-string", value.context))
        return res.success(String(self.value.replace(string.value, value.value)))

    @args(["string"], [String("")])
    @method
    def find(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot find a non-string", string.context))
        return res.success(Number(self.value.find(string.value)))

    @args(["string"], [String("")])
    @method
    def startswith(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(
                RTError(string.pos_start, string.pos_end, "Cannot startswith a non-string", string.context)
            )
        return res.success(Boolean(self.value.startswith(string.value)))

    @args(["string"], [String("")])
    @method
    def endswith(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(
                RTError(string.pos_start, string.pos_end, "Cannot endswith a non-string", string.context)
            )
        return res.success(Boolean(self.value.endswith(string.value)))

    @args(["string"], [String(" ")])
    @method
    def split(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")  # String object
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot split a non-string", string.context))
        return res.success(Array([String(i) for i in self.value.split(str(string))]))

    @args(["string"], [String("")])
    @method
    def join(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot join a non-string", string.context))
        return res.success(String(string.value.join(self.value)))

    @args(["string"], [String("")])
    @method
    def strip(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot strip a non-string", string.context))
        return res.success(String(self.value.strip(string.value)))

    @args(["string"], [String("")])
    @method
    def lstrip(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot lstrip a non-string", string.context))
        return res.success(String(self.value.lstrip(string.value)))

    @args(["string"], [String("")])
    @method
    def rstrip(self, ctx: Context) -> RTResult[Value]:
        res = RTResult[Value]()
        string = ctx.symbol_table.get("string")
        assert string is not None
        if not isinstance(string, String):
            return res.failure(RTError(string.pos_start, string.pos_end, "Cannot rstrip a non-string", string.context))
        return res.success(String(self.value.rstrip(string.value)))
