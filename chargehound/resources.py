from chargehound.api_requestor import APIRequestor

requestor = APIRequestor()


class Disputes(object):
    @classmethod
    def create(klass, dispute_id, **kwargs):
        params = kwargs.pop('query_params', None)
        return requestor.request('post', 'disputes',
                                 data=kwargs, params=params)

    """
    Retrieve a dispute
    This method will return a single dispute.

    :param str dispute_id: A dispute id (required)
    :return: Dispute
    """
    @classmethod
    def retrieve(klass, dispute_id):
        return requestor.request('get', 'disputes/{0}'.format(dispute_id))

    """
    A list of disputes
    This method will list all the disputes that we have synced from Stripe.
    By default the disputes will be ordered by `created`
    with the most recent dispute first.
    `has_more` will be `true` if more results are available.

    :param int limit: Maximum number of disputes to return.
        Default is 20, maximum is 100. (optional)
    :param str starting_after: A dispute id.
        Fetch disputes created after this dispute. (optional)
    :param str ending_before: A dispute id.
        Fetch disputes created before this dispute. (optional)
    :return: Disputes
    """
    @classmethod
    def list(klass, **kwargs):
        list_params = kwargs

        return requestor.request('get', 'disputes',
                                 params=list_params)

    """
    Submitting a dispute
    You will want to submit the dispute through Chargehound after you recieve
    a notification from Stripe of a new dispute.
    With one `POST` request you can update a dispute with the
    evidence fields and send the generated response to Stripe.
    The response will have a `201` status if the submit was successful.
    The dispute will also be in the submitted state.

    :param str dispute_id: A dispute id (required)
    :param str template: Set the template for this dispute. (optional)
    :param object fields:
        Key value pairs to hydrate the template's evidence fields. (optional)
    :param object products:
        List of products the customer purchased. (optional)
    :param str account_id: Set the associated Stripe account id. (optional)
    :param bool force:
        Bypass the manual review filter. (optional)
    :return: Dispute
    """
    @classmethod
    def submit(klass, dispute_id, **kwargs):
        params = kwargs.pop('query_params', None)
        update = kwargs

        return requestor.request('post',
                                 'disputes/{0}/submit'.format(dispute_id),
                                 data=update,
                                 params=params)

    """
    Updating a dispute
    You can update the template and the fields on a dispute.

    :param str dispute_id: A dispute id (required)
    :param str template: Set the template for this dispute. (optional)
    :param object fields:
        Key value pairs to hydrate the template's evidence fields. (optional)
    :param object products:
        List of products the customer purchased. (optional)
    :param str account_id: Set the associated Stripe account id. (optional)
    :return: Dispute
    """
    @classmethod
    def update(klass, dispute_id, **kwargs):
        params = kwargs.pop('query_params', None)
        update = kwargs

        return requestor.request('post', 'disputes/{0}'.format(dispute_id),
                                 data=update,
                                 params=params)
