import graphene


class AcousticDetectorSpecificationInput(graphene.InputObjectType):
    detected_labels = graphene.List(graphene.ID)
    min_frequency = graphene.Int(required=False)
    max_frequency = graphene.Int(required=False)
    algorithm_name = graphene.String(required=False)
