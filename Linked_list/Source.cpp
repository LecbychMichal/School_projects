#include <stdio.h>
#include <stdlib.h>
#include "item.h"

ITEM* list = NULL;

void main()
{
	ITEM* p;
	list_display(list);
	p = (ITEM*)calloc(1, sizeof(ITEM));
	p->data = 333;
	list_add(p, &list);
	list_display(list);

	p = (ITEM*)calloc(1, sizeof(ITEM));
	p->data = 666;
	list_add(p, &list);
	list_display(list);

	p = (ITEM*)calloc(1, sizeof(ITEM));
	p->data = -77;
	list_add(p, &list);
	list_display(list);

	p = (ITEM*)calloc(1, sizeof(ITEM));
	p->data = 1;
	list_add_first(p, &list);
	list_display(list);

	list_add_data(555, &list);
	list_display(list);

	p = list_get_first(&list);
	if (p) {
		printf("get: %d\n", p->data);
	}
	list_display(list);

	p = list_get_last(&list);
	if (p) {
		printf("get: %d\n", p->data);
	}
	list_display(list);

	list_clear(&list);
	list_display(list);
}