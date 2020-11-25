PROTO_DIR=./protos

# APIService
API_PROTO=$(PROTO_DIR)/apiservice.proto
API_OUT=./services/ApiService

# testing
TEST_DIR=./test
API_TEST_OUT=./test/test_ApiService

codegen_api:
	protoc --go_out=$(API_OUT) --go_opt=paths=import \
    --go-grpc_out=$(API_OUT) --go-grpc_opt=paths=import \
    $(API_PROTO)

test: build_test
	python -m unittest discover $(TEST_DIR)
	

build_test:
	python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(API_TEST_OUT) --grpc_python_out=$(API_TEST_OUT) $(API_PROTO)

