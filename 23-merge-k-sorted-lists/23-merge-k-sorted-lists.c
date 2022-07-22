/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* max(struct ListNode** lists, int listsSize,int* notnull)
{   
    int i;
    int min = 10001;
    int pos;
    for(i=0;i<listsSize;i++)
    {
        if(lists[i]!=NULL&&lists[i]->val<min)
        {
            min=lists[i]->val;
            pos = i;
        }
    }
    struct ListNode *temp=lists[pos];
    lists[pos]=lists[pos]->next;
    if(lists[pos]==NULL)
    {
        (*notnull)=(*notnull)-1;
    }
    return temp;
}
struct ListNode* mergeklists(struct ListNode** lists, int listsSize,int notnull)
{
    struct ListNode *head = NULL;
    if(notnull!=0)
    {
        head = max(lists,listsSize,&notnull);
        head->next = mergeklists(lists,listsSize,notnull);
    }
    return head;
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize)
{
    int notnull = listsSize;
    int i;
    for(i=0;i<listsSize;i++)
    {
        if(lists[i]==NULL)
            notnull-=1;
    }
    return mergeklists(lists,listsSize,notnull);   
}