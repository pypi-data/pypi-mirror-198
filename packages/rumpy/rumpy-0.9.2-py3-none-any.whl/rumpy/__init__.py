import datetime
import logging

from rumpy.client import FullNode, HttpRequest, LightNode

__version__ = "0.9.2"
__author__ = "liujuanjuan1984"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
logging.basicConfig(
    format="%(name)s %(asctime)s %(levelname)s %(message)s",
    # filename=f"rumpy_{datetime.date.today()}.log",
    level=logging.INFO,
)
