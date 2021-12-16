#include "list.h"

/**
 * insert_node - inserts a number in a sorted list
 * @head: pointer to head of list
 * @number: number to insert
 * return: pointer to new node or NULL
 * 
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *temp;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;
    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }
    temp = *head;
    while (temp->next != NULL && temp->next->n < number)
        temp = temp->next;
    if (temp->next == NULL)
    {
        temp->next = new_node;
        return (new_node);
    }
    new_node->next = temp->next;
    temp->next = new_node;
    return (new_node);
}
