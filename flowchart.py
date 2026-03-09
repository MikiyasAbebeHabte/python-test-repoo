#           ┌─────────────┐
#           │ Start Loop  │
#           └─────┬──────┘
#                 │
#                 ▼
#      ┌─────────────────────┐
#      │ User types action   │
#      │ ('add','view','complete',│
#      │  'delete','exit')   │
#      └─────────┬──────────┘
#                │
#       ┌────────▼─────────┐
#       │ Is action == exit?│
#       └────────┬─────────┘
#                │Yes
#                ▼
#          ┌──────────┐
#          │ Break    │
#          │ (show    │
#          │ summary) │
#          └──────────┘
#                │No
#                ▼
#       ┌───────────────┐
#       │ Is action =   │
#       │ "add"?        │
#       └───────┬───────┘
#               │Yes
#               ▼
#  ┌───────────────────────────┐
#  │ Ask for task name &       │
#  │ priority (validate input) │
#  │ Append to todo_list       │
#  └────────────┬──────────────┘
#               ▼
#          Go back to loop
#               │
#               ▼
#      ┌───────────────┐
#      │ Is action =   │
#      │ "view"?       │
#      └───────┬───────┘
#              │Yes
#              ▼
#    ┌─────────────────────┐
#    │ Is todo_list empty? │
#    └───────┬────────────┘
#            │Yes
#            ▼
#    ┌─────────────┐
#    │ Print "No   │
#    │ tasks yet"  │
#    └──────┬──────┘
#            │No
#            ▼
#  ┌───────────────────────────────┐
#  │ Print all tasks with index,   │
#  │ priority, and status          │
#  └───────────────┬───────────────┘
#                  ▼
#             Go back to loop
#                  │
#                  ▼
#     ┌───────────────────────┐
#     │ Is action = "complete"?│
#     └───────────┬───────────┘
#                 │Yes
#                 ▼
#     ┌─────────────────────────────┐
#     │ Is todo_list empty?          │
#     └─────────┬───────────────────┘
#               │Yes
#               ▼
#       Print "No tasks to complete"
#               │No
#               ▼
#   Ask for task number → if valid → mark task[2] = True
#               ▼
#            Go back to loop
#               │
#               ▼
#     ┌─────────────────────┐
#     │ Is action = "delete"?│
#     └───────────┬──────────┘
#                 │Yes
#                 ▼
#     ┌─────────────────────────────┐
#     │ Is todo_list empty?          │
#     └─────────┬───────────────────┘
#               │Yes
#               ▼
#       Print "No tasks to delete"
#               │No
#               ▼
#  Ask for task number → if valid → remove task
#               ▼
#            Go back to loop
#               │
#               ▼
#      Else → Print "Invalid action"
#               ▼
#            Go back to loop
#               │
#               ▼
#        ┌───────────────┐
#        │ After exit →  │
#        │ Calculate and │
#        │ print summary │
#        └───────────────┘