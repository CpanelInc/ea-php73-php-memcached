OBS_PROJECT := EA4
OBS_PACKAGE := ea-php73-php-memcached
DISABLE_BUILD += repository=CentOS_9 repository=xUbuntu_22.04
include $(EATOOLS_BUILD_DIR)obs.mk
