# Add line to config file

file_line {'Password no':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no'
}

file_line {'IdentityFile':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school'
}
