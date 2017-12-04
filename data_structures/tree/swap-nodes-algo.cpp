#include <iostream>
using namespace std;
struct node{
  struct node *left;
  struct node *right;
  int data;
};
struct node* getNode(int d){
  if(d==-1) return NULL;
  struct node* n = new node();
  n->data=d;
  n->left=NULL;
  n->right=NULL;
  return n;
}
void insert(struct node *root,int node,int left,int right){
  if(root == NULL ) return ;

  if(root->data==node){
    struct node* lnode = getNode(left);
    struct node* rnode = getNode(right);
    root->left=lnode;
    root->right=rnode;
  }
  else{
    insert(root->left,node,left,right);
    insert(root->right,node,left,right);
  }
}
void swap(struct node *root,int depth,int current){
  if(root==NULL) return;
  if(depth==current){
    struct node *temp = root->left;
    root->left=root->right;
    root->right=temp;
    return;
  }
  else{
    swap(root->left,depth,current+1);
    swap(root->right,depth,current+1);
    return;
  }
}
void inorder(struct node *root){
  if(root==NULL){
      return;
    }
  else{
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
    }
}
int max(int a,int b){
  return a>b?a:b;
}
int height(struct node *root){
  if(root==NULL) return 0;
  else return 1+max(height(root->left),height(root->right));
}
int main(){
  int n;
  cin>>n;
  int i=1;
  struct node *root = getNode(1);
  int left,right;
  while(n--){
    cin>>left>>right;
    insert(root,i,left,right);
    i++;
  }
  //inorder(root);
  //cout<<endl;
  int k,depth;
  cin>>k;
  while(k--){
    cin>>depth;
    int j=1;
    int h=height(root);
    while(depth*j <= h){
      //cout<<"swapping for "<<depth*j<<endl;
      swap(root,depth*j,1);
      j+=1;
    }
    //swap(root,depth,1);
    inorder(root);
    cout<<endl;
  }
  return 0;
}
