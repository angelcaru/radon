from core.builtin_classes.base_classes import BuiltInClass
from core.builtin_funcs import global_symbol_table
from core.builtin_classes.file_object import FileObject
from core.builtin_classes.string_object import StringObject


global_symbol_table.set("File", BuiltInClass("File", FileObject))
global_symbol_table.set("String", BuiltInClass("String", StringObject))
