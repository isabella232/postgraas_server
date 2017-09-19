import os
import uuid
import json
import ConfigParser
import StringIO
import pytest

import postgraas_server.backends.postgres_cluster.postgres_cluster_driver as pgcd

def test_get_normalized_username():
    username_with_host = 'testuser1234@testcluster1'
    stripped_username = pgcd.get_normalized_username(username_with_host)
    assert stripped_username == "testuser1234"