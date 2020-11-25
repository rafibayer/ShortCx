PROTO_DIR=./protos

# APIService
API_PROTO=$(PROTO_DIR)/apiservice.proto
API_OUT=./services/ApiService


codegen_api:
	protoc --go_out=$(API_OUT) --go_opt=paths=import \
    --go-grpc_out=$(API_OUT) --go-grpc_opt=paths=import \
    $(API_PROTO)