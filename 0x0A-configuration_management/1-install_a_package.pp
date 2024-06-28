## A puppet file that installs a package
## Specifically Flask
package {'Flask':
      ensure => '2.1.0',
      name   => 'flask',
    provider => 'pip3',
}

package {'Werkzeug':
  ensure   => '2.1.1',
  name     => 'Werkzeug',
  provider => 'pip3',
}
