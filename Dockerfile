FROM fluent/fluentd:v1.12.0-debian-1.0
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.0.3"]
RUN ["fluent-gem", "install", "fluent-plugin-rewrite-tag-filter"]
# RUN gem install fluent-plugin-elasticsearch --no-document --version 5.0.3 && fluent-gem install fluent-plugin-rewrite-tag-filter
USER fluent