# Bachelorproef

Dit project kan worden gerunned met de simpele commandos
`vagrant up` 
en
`vagrant ssh control`
hierna moet enkel
`cv /vagrant/ansible`
en 
`ansible-galaxy install -r requirements.yml`
worden uitgevoerd

Ten slotte moeten de playbooks gerunned worden met
```
ansible-playbook -i intentory.yml site.yml
ansible-playbook -i intentory.yml router-config.yml
```

In ansible/group_vars/all.yml moet er een file gemaakt worden 
```
# group_vars/all.yml
# Variables visible to all nodes
---
rhbase_users:
  - name: 
    password:   # Can a tool like `mkpasswd` to generate the hashed password
    groups:
      - wheel
    ssh_key: 
```

Eenmaal opgestart kan je via Grafana naar contactpoints gaan, en de alertmanager toevoegen van http://localhost:9093

