#Install package

exec { 'install flask':
  command => 'pip3 install flask',
  path    => '/usr/bin',
  version => '2.1.0',
}
