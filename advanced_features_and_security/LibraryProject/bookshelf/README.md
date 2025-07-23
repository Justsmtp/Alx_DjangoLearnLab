# Permissions & Groups Setup

## Custom Permissions on Book Model
Defined in `Book.Meta.permissions`:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created using Django signals (`signals.py`):
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

## Usage in Views
Each view is protected with `@permission_required()` to ensure access control.

## Testing
Use Django Admin to assign users to groups. Try logging in as different users and verify restricted actions.
