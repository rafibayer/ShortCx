FROM golang:1.14-alpine
RUN mkdir -p /server
WORKDIR /server
ADD . /server
EXPOSE 9092
RUN go build ./main.go
CMD ["./main"]