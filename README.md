# docker-raspi-ip-notifier

This container sends network information of host server using gmail account on boot.

# Repository
https://github.com/yamaryoxxxx/docker-raspi-ip-notifier/

# Registory
https://hub.docker.com/r/yamaryoxxxx/raspi-ip-notifier/

# Usage

```
$ docker run
      --rm --net=host 
      -e SEND_FROM=my_account@gmail.com
      -e PASSWORD=password_for_sender
      -e SEND_TO=someone@some.domain
      yamaryoxxxx/raspi-ip-notifier
```
