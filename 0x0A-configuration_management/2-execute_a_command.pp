# Kill Process
exec { 'kill process':
  command => 'pkill killmenow',
}