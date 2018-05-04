# docker-raspi-ip-notifier

This container sends network information of host server using gmail account on boot.

https://github.com/yamaryoxxxx/docker-raspi-ip-notifier/

https://hub.docker.com/r/yamaryoxxxx/raspi-ip-notifier/

## Usage

The following enables automatic IP notification of Raspberry Pi on its boot.

```
$ docker run
      -d --restart=always --net=host 
      -e SEND_FROM=my_account@gmail.com
      -e SEND_PASSWORD=password_for_sender
      -e SEND_TO=someone@some.domain
      -e WAIT=15
      yamaryoxxxx/raspi-ip-notifier
```
