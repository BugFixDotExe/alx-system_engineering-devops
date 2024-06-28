## A puppet script that kills a process
exec {'killmenow':
  command => '/usr/bin/pkill killmenow',
}
