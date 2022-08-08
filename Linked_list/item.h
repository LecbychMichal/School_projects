#pragma once


struct ITEM {
	ITEM* next;
	int data;
};

void list_display(ITEM*);
void list_add(ITEM* p, ITEM** list);
void list_add_first(ITEM* p, ITEM** list);
void list_add_data(int d, ITEM** list);
ITEM* list_get_first(ITEM** list);
ITEM* list_get_last(ITEM** list);
void list_clear(ITEM** list);