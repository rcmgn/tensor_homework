FROM alpine:3.14
RUN apk update && apk upgrade && apk add pv
CMD (pv -n /dev/random | dd of=/file.tmp bs=1024 count=1000000 oflag=direct) 2>/vol/out.txt
