#include <iostream>
using namespace std;

class SLL {
private:
    struct node {
        int data;
        node *next;
    };
    node *start;

public:
    SLL() {
        start = NULL;
    }

    void create();
    void display();
};

void SLL::create() {
    int ans;
    node *temp, *curr;

    do {
        temp = new node;
        temp->next = NULL;

        cout << "\nEnter data: ";
        cin >> temp->data;

        if (start == NULL) {
            start = temp;
            curr = temp;
        } else {
            curr->next = temp;
            curr = temp;
        }

        cout << "Do you want to add more nodes? (1 for Yes / 0 for No): ";
        cin >> ans;

    } while (ans == 1);
}

void SLL::display() {
    if (start == NULL) {
        cout << "\nSLL is empty!";
        return;
    }

    node *t = start;
    cout << "\nSingly Linked List elements: ";
    while (t != NULL) {
        cout << t->data << " -> ";
        t = t->next;
    }
    cout << "NULL\n";
}

int main() {
    SLL a;
    a.create();
    a.display();
    return 0;
}
