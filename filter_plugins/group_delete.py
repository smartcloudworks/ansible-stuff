# This is an Ansible filter that will remove a
# group from a member.
#
# Groups in Ansible can be retrieved using the
# command module.
# command:
#   cmd: groups user
# register: group_results
#
# Results should resemble the following:
# user : user wheel devs dbadmins
#
# Results can be filtered using the below code
# ex. group_results['stdout'] | remove_groups(wheel)
#
# Multiple groups can also be removed if deliminated
# with a comma.
# ex. group_results['stdout'] | remove_groups(wheel,devs)
#
# Finally, the returned string should resemble the following
# user,dbadmins
#
# From here, you can use the ansible.builtin.user module to
# assign the groups to the members. If append=no, then user
# will be removed from groups not part of the returned values.

class FilterModule(object):
  def filters(self):
    return {'remove_groups': self.del_group}

  def del_group(self, gresults, *gremove):

    # This will split the string into a list of 2,
    #   using the : to split.
    tmp_list = gresults['stdout'].split(":")

    # This splits the second list item into another
    #   list, where each group is its own list item.
    tmp_list = tmp_list[1].split()

    # This iterates through the groups that are to
    #   be removed, and it removes them.
    for g in gremove:
      if g in tmp_list:
        tmp_list.remove(g)

    # This combines the new list of groups into a string
    #   that can be easily passed to the user module.
    return ",".join(tmp_list)
