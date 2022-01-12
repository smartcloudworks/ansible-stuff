---
- hosts: "{{ nodes }}"

  tasks:

    - name: Create User
      user:
        name: "{{ user }}"
        comment: "{{ comment | default(omit) }}"
        shell: "{{ shell | default(omit) }}"
        state: present
