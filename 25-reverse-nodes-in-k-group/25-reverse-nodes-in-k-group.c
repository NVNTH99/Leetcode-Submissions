/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseKGroup(struct ListNode* head, int k)
{
     if(head==NULL)
        return NULL;
    int i=1;
    struct ListNode *x,*a,*b,*c;
    x=head;
    while(i!=k&&x!=NULL)
    {
        x=x->next;
        i++;
    }
    if(i==k&&x!=NULL)
    {
        a=x->next;
        b=head;
        c=head->next;
        head=x;
        x=b;
        while(a!=head)
        {
            b->next=a;
            a=b;
            b=c;
            if(c!=NULL)
                c=c->next;
        }
        x->next = reverseKGroup(b,k);
    }
    return head;
}