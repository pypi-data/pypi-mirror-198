#ifndef HEADER_CURL_CF_SOCKET_H
#define HEADER_CURL_CF_SOCKET_H
/***************************************************************************
 *                                  _   _ ____  _
 *  Project                     ___| | | |  _ \| |
 *                             / __| | | | |_) | |
 *                            | (__| |_| |  _ <| |___
 *                             \___|\___/|_| \_\_____|
 *
 * Copyright (C) Daniel Stenberg, <daniel@haxx.se>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution. The terms
 * are also available at https://curl.se/docs/copyright.html.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 * SPDX-License-Identifier: curl
 *
 ***************************************************************************/
#include "curl_setup.h"

#include "nonblock.h" /* for curlx_nonblock(), formerly Curl_nonblock() */
#include "sockaddr.h"

struct Curl_addrinfo;
struct Curl_cfilter;
struct Curl_easy;
struct connectdata;
struct Curl_sockaddr_ex;

/*
 * The Curl_sockaddr_ex structure is basically libcurl's external API
 * curl_sockaddr structure with enough space available to directly hold any
 * protocol-specific address structures. The variable declared here will be
 * used to pass / receive data to/from the fopensocket callback if this has
 * been set, before that, it is initialized from parameters.
 */
struct Curl_sockaddr_ex {
  int family;
  int socktype;
  int protocol;
  unsigned int addrlen;
  union {
    struct sockaddr addr;
    struct Curl_sockaddr_storage buff;
  } _sa_ex_u;
};
#define sa_addr _sa_ex_u.addr


/*
 * Create a socket based on info from 'conn' and 'ai'.
 *
 * Fill in 'addr' and 'sockfd' accordingly if OK is returned. If the open
 * socket callback is set, used that!
 *
 */
CURLcode Curl_socket_open(struct Curl_easy *data,
                            const struct Curl_addrinfo *ai,
                            struct Curl_sockaddr_ex *addr,
                            int transport,
                            curl_socket_t *sockfd);

int Curl_socket_close(struct Curl_easy *data, struct connectdata *conn,
                      curl_socket_t sock);

/*
 * This function should return TRUE if the socket is to be assumed to
 * be dead. Most commonly this happens when the server has closed the
 * connection due to inactivity.
 */
bool Curl_socket_is_dead(curl_socket_t sock);

/**
 * Determine the curl code for a socket connect() == -1 with errno.
 */
CURLcode Curl_socket_connect_result(struct Curl_easy *data,
                                    const char *ipaddress, int error);

#ifdef USE_WINSOCK
/* When you run a program that uses the Windows Sockets API, you may
   experience slow performance when you copy data to a TCP server.

   https://support.microsoft.com/kb/823764

   Work-around: Make the Socket Send Buffer Size Larger Than the Program Send
   Buffer Size

*/
void Curl_sndbufset(curl_socket_t sockfd);
#else
#define Curl_sndbufset(y) Curl_nop_stmt
#endif

/**
 * Assign the address `ai` to the Curl_sockaddr_ex `dest` and
 * set the transport used.
 */
void Curl_sock_assign_addr(struct Curl_sockaddr_ex *dest,
                           const struct Curl_addrinfo *ai,
                           int transport);

/**
 * Creates a cfilter that opens a TCP socket to the given address
 * when calling its `connect` implementation.
 * The filter will not touch any connection/data flags and can be
 * used in happy eyeballing. Once selected for use, its `_active()`
 * method needs to be called.
 */
CURLcode Curl_cf_tcp_create(struct Curl_cfilter **pcf,
                            struct Curl_easy *data,
                            struct connectdata *conn,
                            const struct Curl_addrinfo *ai,
                            int transport);

/**
 * Creates a cfilter that opens a UDP socket to the given address
 * when calling its `connect` implementation.
 * The filter will not touch any connection/data flags and can be
 * used in happy eyeballing. Once selected for use, its `_active()`
 * method needs to be called.
 */
CURLcode Curl_cf_udp_create(struct Curl_cfilter **pcf,
                            struct Curl_easy *data,
                            struct connectdata *conn,
                            const struct Curl_addrinfo *ai,
                            int transport);

/**
 * Creates a cfilter that opens a UNIX socket to the given address
 * when calling its `connect` implementation.
 * The filter will not touch any connection/data flags and can be
 * used in happy eyeballing. Once selected for use, its `_active()`
 * method needs to be called.
 */
CURLcode Curl_cf_unix_create(struct Curl_cfilter **pcf,
                             struct Curl_easy *data,
                             struct connectdata *conn,
                             const struct Curl_addrinfo *ai,
                             int transport);

/**
 * Creates a cfilter that keeps a listening socket.
 */
CURLcode Curl_conn_tcp_listen_set(struct Curl_easy *data,
                                  struct connectdata *conn,
                                  int sockindex,
                                  curl_socket_t *s);

/**
 * Replace the listen socket with the accept()ed one.
 */
CURLcode Curl_conn_tcp_accepted_set(struct Curl_easy *data,
                                    struct connectdata *conn,
                                    int sockindex,
                                    curl_socket_t *s);

/**
 * Return TRUE iff `cf` is a socket filter.
 */
bool Curl_cf_is_socket(struct Curl_cfilter *cf);

/**
 * Peek at the socket and remote ip/port the socket filter is using.
 * The filter owns all returned values.
 * @param psock             pointer to hold socket descriptor or NULL
 * @param paddr             pointer to hold addr reference or NULL
 * @param pr_ip_str         pointer to hold remote addr as string or NULL
 * @param pr_port           pointer to hold remote port number or NULL
 * @param pl_ip_str         pointer to hold local addr as string or NULL
 * @param pl_port           pointer to hold local port number or NULL
 * Returns error if the filter is of invalid type.
 */
CURLcode Curl_cf_socket_peek(struct Curl_cfilter *cf,
                             struct Curl_easy *data,
                             curl_socket_t *psock,
                             const struct Curl_sockaddr_ex **paddr,
                             const char **pr_ip_str, int *pr_port,
                             const char **pl_ip_str, int *pl_port);

extern struct Curl_cftype Curl_cft_tcp;
extern struct Curl_cftype Curl_cft_udp;
extern struct Curl_cftype Curl_cft_unix;
extern struct Curl_cftype Curl_cft_tcp_accept;

#endif /* HEADER_CURL_CF_SOCKET_H */
