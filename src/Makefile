PROTO_DIR=./protos

# APIService
API_PROTO=$(PROTO_DIR)/apiservice.proto
API_OUT=./services/ApiService

# AuthService
AUTH_PROTO=$(PROTO_DIR)/authservice.proto
AUTH_OUT=./services/AuthService/server

# testing
TEST_DIR=./test
API_TEST_OUT=./test/test_ApiService

# Generate Code for APIService
codegen_api:
	# APIService
	protoc -I=$(PROTO_DIR) --go_out=$(API_OUT) --go_opt=paths=import \
    --go-grpc_out=$(API_OUT) --go-grpc_opt=paths=import \
    $(API_PROTO)

	protoc -I=$(PROTO_DIR) --go_out=$(API_OUT) --go_opt=paths=import \
    --go-grpc_out=$(API_OUT) --go-grpc_opt=paths=import \
    $(AUTH_PROTO)
	

codegen_auth:
	#AuthService
	python -m grpc_tools.protoc -I=$(PROTO_DIR) \
	--python_out=$(AUTH_OUT) \
	--grpc_python_out=$(AUTH_OUT) \
	$(AUTH_PROTO)

	# APIService (.proto import dependency)
	python -m grpc_tools.protoc -I=$(PROTO_DIR) \
	--python_out=$(AUTH_OUT) \
	--grpc_python_out=$(AUTH_OUT) \
	$(API_PROTO)

# Run all unittests (currently broken until someone answers my stackoverflow)
# in the meantime, test files can be run manually
test: build_test
	python -m unittest discover $(TEST_DIR)
	

# Generate all code needed for test clients
build_test:
	python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(API_TEST_OUT) --grpc_python_out=$(API_TEST_OUT) $(API_PROTO)

