#include <stdio.h>
#include <stdlib.h>

struct node{
	int data; // Stores the data value
	struct node * next; // pointer to next node
};

// Insert At the Beginning
struct node* insert_at_beginning(struct node *head, int data) {
	struct node *new_node = malloc(sizeof(struct node));

	new_node->data = data;
	new_node->next = head;

	return new_node;
}

struct node* insert_at_end(struct node *head, int data){
	struct node *new_node = malloc(sizeof(struct node));

	new_node->data = data;
	new_node->next = NULL;

	if (head == NULL)
		return new_node;

		struct node *current = head;
		while(current->next !=NULL){
			current = current->next;
		}
		current->next = new_node;
		return head;
}

void display(struct node *head){
	struct node *current = head;

	while(current !=NULL){
		printf("%d ->",current->data);
		current = current->next;
	}
	printf("NULL \n");
}

int main(void){
	
	struct node *head = NULL;

	head = insert_at_beginning(head, 20);
    head = insert_at_beginning(head, 10);

    head = insert_at_end(head, 30);
    head = insert_at_end(head, 40);

    display(head);
	return 0;
}
