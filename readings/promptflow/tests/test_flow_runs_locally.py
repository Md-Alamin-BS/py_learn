from promptflow.client import PFClient


# check that the flow can run locally without error
def test_eval_flow_runs_locally():
    """Make sure that the eval flow can run locally without error."""
    pfclient = PFClient()
    # If an exception is raised the test will fail
    pfclient.flows.test(
        flow="flows/evaluation",
        allow_generator_output=False,
        stream_output=False,
        dump_test_result=True,
    )
