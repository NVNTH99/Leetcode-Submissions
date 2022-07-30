/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


bool isPalindrome(struct ListNode* head){
    struct ListNode *x;
    x=head;
    int l=1;
    while(x->next!=NULL)
    {
        x=x->next;
        l++;
    }
    int arr[l];
    int i;
    x=head;
    for(i=0;i<l;i++)
    {
        arr[i]=x->val;
        x=x->next;
    }
    x=head;
    for(i=l-1;i>=0;i--)
    {
        if(arr[i]!=x->val)
            return false;
        x=x->next;
    }
    return true;
}