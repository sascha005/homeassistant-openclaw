ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.7
FROM ${BUILD_FROM}

# Home Assistant add-on base is Alpine.
# Install nodejs + npm, then install OpenClaw.
RUN apk add --no-cache nodejs npm bash curl jq

RUN npm install -g openclaw

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
