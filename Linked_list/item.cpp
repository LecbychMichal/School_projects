#include "item.h"
#include <stdio.h>
#include <stdlib.h>

void list_display(ITEM* list)
{
	ITEM* p = list;
	printf("**START\n");
	while (p) {
		printf("%d\n", p->data);
		p = p->next;
	}

	printf("**END\n");
}

void list_add(ITEM* item, ITEM** list)
{
	ITEM* p = *list;
	item->next = NULL;
	if (!*list) {
		*list = item;
		return;
	}
	while (p->next)
		p = p->next;
	p->next = item;
}

void list_add_first(ITEM* item, ITEM** list)
{
	item->next = *list;
	*list = item;
}

void list_add_data(int d, ITEM** list)
{
	ITEM* p = (ITEM*)calloc(1, sizeof(ITEM));
	p->data = d;
	list_add(p, list);
}

ITEM* list_get_first(ITEM** list)
{
	ITEM* p = *list;
	if (p) {
		*list = p->next;
		p->next = NULL;
	}
	return p;
}

ITEM* list_get_last(ITEM** list)
{
	ITEM* p = *list, * p1;
	if(!p)
		return NULL;
	if (!p->next) {
		*list = NULL;
		return p;
	}
	p1 = p;
	p = p->next;
	while (p->next) {
		p1 = p;
		p = p->next;
	}
	p1->next = NULL;
	return p;
}

void list_clear(ITEM** list) {
	ITEM* p;
	while (p = list_get_first(list)) {
		free(p);
	}
}