#include <stdio.h>
#include <Python.h>
/**
* print_python_list_info - prints python list info
* @p: is a PyObject
* Return: no return
*/
void print_python_list_info(PyObject *p)
{
long int s, y;
PyListObject *list;
PyObject *item;
s = Py_SIZE(p);
printf("[*] Size of the Python List = %ld\n", s);
list = (PyListObject *)p;
printf("[*] Allocated = %ld\n", list->allocated);
for (y = 0; y < s; y++)
{
item = PyList_GetItem(p, y);
printf("Element %ld: %s\n", y, Py_TYPE(item)->tp_name);
}
}
