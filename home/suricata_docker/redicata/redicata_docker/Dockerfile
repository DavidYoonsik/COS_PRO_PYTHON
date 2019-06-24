FROM centos:7

RUN yum-config-manager --enable cr
RUN yum -y install epel-release

RUN ldconfig

RUN yum install -y sudo GeoIP-devel hiredis hiredis-devel python-devel openssl-devel lrzsz net-tools wget git flex bison gcc gcc-c++ make  libpcap libpcap-devel libnet libnet-devel pcre pcre-devel automake autoconf libtool libyaml libyaml-devel numactl-devel zlib zlib-devel jansson-devel file file-devel subversion hiredis nss* nspr* ncurses-devel "Development Tools" hmaccalc zlib-devel binutils-devel elfutils-libelf-devel cmake3 libquadmath-devel bzip2-devel sqlite-devel rust* cargo* lz4* ragel*

RUN cargo install cargo-vendor --force
RUN mkdir -p /home/work
COPY suricata.yaml /home/work/suricata.yaml
RUN mkdir -p /usr/local/etc/suricata
COPY *.config /usr/local/etc/suricata/
RUN mkdir -p /usr/local/etc/suricata/rules
COPY rules/* /usr/local/etc/suricata/rules/
RUN cd /home/work && wget -o -L https://www.openinfosecfoundation.org/download/suricata-5.0.0-beta1.tar.gz
RUN cd /home/work && tar -xzf suricata-*.tar.gz
RUN cd /home/work && rm -rf suricata-*.tar.gz


## suricata install
RUN cd /home/work/suricata-5.0.0-beta1 && ./configure --enable-rust --enable-python --enable-geoip --enable-hiredis --with-libnss-libraries=/usr/lib --with-libnss-includes=/usr/include/nss3 --with-libnspr-libraries=/usr/lib --with-libnspr-includes=/usr/include/nspr4 --with-libhiredis-libraries=/usr/lib64 --with-libhiredis-includes=/usr/include/hiredis && make -j 4 && make install -j 4

RUN PATH="/root/.cargo/bin:$PATH"
RUN export PATH

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh && ldconfig 

RUN suricata --build-info

ENTRYPOINT ["/docker-entrypoint.sh"]

