/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverse(struct ListNode* prev,struct ListNode* head,struct ListNode* p)
{
    head->next=prev;
    if(p==NULL)
        return head;
    return reverse(head,p,p->next);
}
int value(struct ListNode* head)
{
    if(head==NULL)
        return 0;
    return head->val;
}
struct ListNode* insert(struct ListNode* l1,struct ListNode* l2,int carry)
{
    if(l1==NULL&&l2==NULL&&carry==0)
        return NULL;
    int sum;
    sum = value(l1)+value(l2)+carry;
    struct ListNode *x;
    x=(struct ListNode*)malloc(sizeof(struct ListNode));
    x->val = sum%10;
    if(l1!=NULL)
        l1=l1->next;
    if(l2!=NULL)
        l2=l2->next;
    x->next = insert(l1,l2,sum/10);
    return x;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    l1 = reverse(NULL,l1,l1->next);
    l2 = reverse(NULL,l2,l2->next);
    struct ListNode *head=NULL;
    head = insert(l1,l2,0);
    head =  reverse(NULL,head,head->next);
    return head;
}