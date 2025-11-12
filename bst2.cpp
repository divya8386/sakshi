#include <iostream>
using namespace std;

class BST {
private:
    struct node {
        int data;
        node *lc;
        node *rc;
    };
    node *root;

public:
    BST() {
        root = NULL;
    }

    void create();
    void display();

private:
    void rec_preorder(node *t);
};

void BST::create() {
    int ans;
    node *temp, *curr;

    do {
        temp = new node;
        temp->lc = NULL;
        temp->rc = NULL;

        cout << "Enter data: ";
        cin >> temp->data;

        if (root == NULL) {
            root = temp;
        } else {
            curr = root;
            while (true) {
                if (temp->data < curr->data) {
                    if (curr->lc == NULL) {
                        curr->lc = temp;
                        break;
                    } else {
                        curr = curr->lc;
                    }
                } else {
                    if (curr->rc == NULL) {
                        curr->rc = temp;
                        break;
                    } else {
                        curr = curr->rc;
                    }
                }
            }
        }

        cout << "Add one more node? (1-Yes / 0-No): ";
        cin >> ans;

    } while (ans == 1);
}

void BST::display() {
    cout << "\nPreorder traversal: ";
    rec_preorder(root);
    cout << endl;
}

void BST::rec_preorder(node *t) {
    if (t == NULL)
        return;
    cout << " " << t->data;
    rec_preorder(t->lc);
    rec_preorder(t->rc);
}

int main() {
    BST b;
    b.create();
    b.display();
    return 0;
}
