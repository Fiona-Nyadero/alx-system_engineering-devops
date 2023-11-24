# kill a process
exec { 'killmenow_process':
  command  => 'pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
