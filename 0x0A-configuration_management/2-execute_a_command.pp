# Kill Process
exec { 'kill process':
  path    => '/usr/bin/',
  command => 'pkill killmenow',
}