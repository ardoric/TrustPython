# TrustPython

A sample web application showing how TLS trust issues can be overcome via code in Python.

The pages will make a request to a server with an untrusted root (https://untrusted-root.badssl.com), hash that content and show it on the page.

This is useful, for example, in multi-tenant App Service offering.

All the code is in TrustPython/views.py file

## badssl.crt

This file has the root certificate being used by the external server. As far as I can tell, it has to be in the base64 format. Python will not properly load a binary .cer file.

## fail_request

A normal request that will fail due to there being no special code

## call_requests

Uses the badssl.crt file in the verify parameter of requests to specify this certificate should be used

## urllib3 solution

I did not investigate this much. I feel like requests is the more used library, but feel free to reach out if you need help with this one.

Also, since requests apparently uses urllib3 in the backend, it is possible a urllib3 general solution would also magically work for requests.

## Other considerations

If you are contacting several servers you can either be explicit with each call, or bundle all the certificates in the same "extra CAs" file, probably.

