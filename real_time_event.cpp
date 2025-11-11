#include <iostream>
#include <string>
using namespace std;

string event[5];
int F = -1;
int R = -1;
int max_size = 5;

// Function to add event (enqueue)
void AddEvent() {
    if (R == max_size - 1) {
        cout << "Queue Overflow! Cannot add more events.\n";
    } else {
        string name;
        cout << "Enter event name: ";
        cin >> name;
        if (F == -1) {
            F = R = 0;
        } else {
            R++;
        }
        event[R] = name;
        cout << "Event added successfully.\n";
    }
}

// Function to process next event (dequeue from front)
void ProcessNextEvent() {
    if (F == -1) {
        cout << "No events to process!\n";
    } else {
        cout << "Processing event: " << event[F] << endl;
        if (F == R) {
            // last event processed, reset queue
            F = R = -1;
        } else {
            F++;
        }
    }
}

// Function to cancel event (similar to dequeue)
void CancelEvent() {
    if (F == -1) {
        cout << "No events present in the queue.\n";
    } else {
        cout << "Cancelled event: " << event[F] << endl;
        if (F == R) {
            F = R = -1;
        } else {
            F++;
        }
    }
}

// Function to display events
void DisplayEvent() {
    if (F == -1) {
        cout << "No events to display!\n";
    } else {
        cout << "Events in queue:\n";
        for (int i = F; i <= R; i++) {
            cout << i - F + 1 << ". " << event[i] << endl;
        }
    }
}

int main() {
    int choice;
    string more;
    do {
        cout << "\n--- MENU ---\n";
        cout << "1. Add Event\n";
        cout << "2. Process Next Event\n";
        cout << "3. Cancel Event\n";
        cout << "4. Display Events\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                AddEvent();
                break;
            case 2:
                ProcessNextEvent();
                break;
            case 3:
                CancelEvent();
                break;
            case 4:
                DisplayEvent();
                break;
            case 5:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }

        if (choice != 5) {
            cout << "Do you want to continue? (yes/no): ";
            cin >> more;
        }
    } while (choice != 5 && (more == "yes" || more == "Yes"));

    return 0;
}
