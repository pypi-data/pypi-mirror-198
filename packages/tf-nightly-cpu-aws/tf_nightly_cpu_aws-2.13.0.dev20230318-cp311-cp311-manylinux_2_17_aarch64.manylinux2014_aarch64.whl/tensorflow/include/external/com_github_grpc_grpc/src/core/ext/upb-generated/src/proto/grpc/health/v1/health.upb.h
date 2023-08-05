/* This file was generated by upbc (the upb compiler) from the input
 * file:
 *
 *     src/proto/grpc/health/v1/health.proto
 *
 * Do not edit -- your changes will be discarded when the file is
 * regenerated. */

#ifndef SRC_PROTO_GRPC_HEALTH_V1_HEALTH_PROTO_UPB_H_
#define SRC_PROTO_GRPC_HEALTH_V1_HEALTH_PROTO_UPB_H_

#include "upb/generated_util.h"
#include "upb/msg.h"
#include "upb/decode.h"
#include "upb/encode.h"

#include "upb/port_def.inc"

#ifdef __cplusplus
extern "C" {
#endif

struct grpc_health_v1_HealthCheckRequest;
struct grpc_health_v1_HealthCheckResponse;
typedef struct grpc_health_v1_HealthCheckRequest grpc_health_v1_HealthCheckRequest;
typedef struct grpc_health_v1_HealthCheckResponse grpc_health_v1_HealthCheckResponse;
extern const upb_msglayout grpc_health_v1_HealthCheckRequest_msginit;
extern const upb_msglayout grpc_health_v1_HealthCheckResponse_msginit;

typedef enum {
  grpc_health_v1_HealthCheckResponse_UNKNOWN = 0,
  grpc_health_v1_HealthCheckResponse_SERVING = 1,
  grpc_health_v1_HealthCheckResponse_NOT_SERVING = 2,
  grpc_health_v1_HealthCheckResponse_SERVICE_UNKNOWN = 3
} grpc_health_v1_HealthCheckResponse_ServingStatus;


/* grpc.health.v1.HealthCheckRequest */

UPB_INLINE grpc_health_v1_HealthCheckRequest *grpc_health_v1_HealthCheckRequest_new(upb_arena *arena) {
  return (grpc_health_v1_HealthCheckRequest *)upb_msg_new(&grpc_health_v1_HealthCheckRequest_msginit, arena);
}
UPB_INLINE grpc_health_v1_HealthCheckRequest *grpc_health_v1_HealthCheckRequest_parse(const char *buf, size_t size,
                        upb_arena *arena) {
  grpc_health_v1_HealthCheckRequest *ret = grpc_health_v1_HealthCheckRequest_new(arena);
  return (ret && upb_decode(buf, size, ret, &grpc_health_v1_HealthCheckRequest_msginit, arena)) ? ret : NULL;
}
UPB_INLINE char *grpc_health_v1_HealthCheckRequest_serialize(const grpc_health_v1_HealthCheckRequest *msg, upb_arena *arena, size_t *len) {
  return upb_encode(msg, &grpc_health_v1_HealthCheckRequest_msginit, arena, len);
}

UPB_INLINE upb_strview grpc_health_v1_HealthCheckRequest_service(const grpc_health_v1_HealthCheckRequest *msg) { return UPB_FIELD_AT(msg, upb_strview, UPB_SIZE(0, 0)); }

UPB_INLINE void grpc_health_v1_HealthCheckRequest_set_service(grpc_health_v1_HealthCheckRequest *msg, upb_strview value) {
  UPB_FIELD_AT(msg, upb_strview, UPB_SIZE(0, 0)) = value;
}

/* grpc.health.v1.HealthCheckResponse */

UPB_INLINE grpc_health_v1_HealthCheckResponse *grpc_health_v1_HealthCheckResponse_new(upb_arena *arena) {
  return (grpc_health_v1_HealthCheckResponse *)upb_msg_new(&grpc_health_v1_HealthCheckResponse_msginit, arena);
}
UPB_INLINE grpc_health_v1_HealthCheckResponse *grpc_health_v1_HealthCheckResponse_parse(const char *buf, size_t size,
                        upb_arena *arena) {
  grpc_health_v1_HealthCheckResponse *ret = grpc_health_v1_HealthCheckResponse_new(arena);
  return (ret && upb_decode(buf, size, ret, &grpc_health_v1_HealthCheckResponse_msginit, arena)) ? ret : NULL;
}
UPB_INLINE char *grpc_health_v1_HealthCheckResponse_serialize(const grpc_health_v1_HealthCheckResponse *msg, upb_arena *arena, size_t *len) {
  return upb_encode(msg, &grpc_health_v1_HealthCheckResponse_msginit, arena, len);
}

UPB_INLINE int32_t grpc_health_v1_HealthCheckResponse_status(const grpc_health_v1_HealthCheckResponse *msg) { return UPB_FIELD_AT(msg, int32_t, UPB_SIZE(0, 0)); }

UPB_INLINE void grpc_health_v1_HealthCheckResponse_set_status(grpc_health_v1_HealthCheckResponse *msg, int32_t value) {
  UPB_FIELD_AT(msg, int32_t, UPB_SIZE(0, 0)) = value;
}

#ifdef __cplusplus
}  /* extern "C" */
#endif

#include "upb/port_undef.inc"

#endif  /* SRC_PROTO_GRPC_HEALTH_V1_HEALTH_PROTO_UPB_H_ */
