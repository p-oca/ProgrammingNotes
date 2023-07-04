# This script lists takes the given groups as keys and users as values and returns a dictionary containing the
# relating the users as keys and the groups they are a part of as values.

def groups_per_user(group_dictionary):
    user_groups = {}

    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:  # iterate through users in group_dictionary, using the iterator "user"
            if user not in user_groups:  # check if the currently considered user exists in the returnable "user_groups"
                user_groups[user] = []  # if not, create a new, blank entry
            user_groups[user].append(group)

    return user_groups


print(groups_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"]
}))