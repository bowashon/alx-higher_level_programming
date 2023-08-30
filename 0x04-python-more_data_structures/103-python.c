#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - function that prints python bytes
 * @p: python object
 *
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int len, i, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf(" len: %ld\n", len);
	printf(" trying string: %s\n", str);

	lim = len > 10 ? 10 : len;
	printf(" first %ld bytes:", lim);

	for (i = 0; i < lim; i++)
	{
		if (str[i] >= 0)
			printf(" %02x", (unsigned char)str[i]);
		else
			printf(" %02x", 256 + (unsigned char)str[i]);
	}
	putchar('\n');
}

/**
 * print_python_list - function that print function list
 * @p: python object
 *
 */
void print_python_list(PyObject *p)
{
	long int len, i;
	PyListObject *list;
	PyObject object;

	len = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < len; i++)
	{
		object = list->ob_item[i];
		printf("Element %ld: %s\n",  i,
		((PyTypeObject *)(object->ob_type))->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
