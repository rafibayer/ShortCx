PROTO_DIR=./protos

# APIService
API_PROTO=$(PROTO_DIR)/apiservice.proto
API_OUT=./services/ApiService
API_GRPC_OUT=./services/ApiService

codegen_api:
	protoc --go_out=$(API_OUT) --go_opt=paths=source_relative \
    --go-grpc_out=$(API_GRPC_OUT) --go-grpc_opt=paths=source_relative \
   $(API_PROTO)