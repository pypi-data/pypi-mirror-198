# Validation Codes Dictionary

## Information

### info.excluded

**Message:** User excluded S-P-O triple '{identifier}' or all test case S-P-O triples from resource test location.

**Description:** Check the JSON KP test edge data file for specific 'exclude_tests' directives, either global to the file, or on specific edges.

### info.compliant

**Message:** Biolink Model-compliant TRAPI Message.

**Description:** Specified TRAPI message completely satisfies the target TRAPI schema and Biolink Model semantics for specified releases of these standards.

### info.input_edge.predicate.abstract

**Message:** Input Edge '{edge_id}' has an 'abstract' predicate '{identifier}'.

**Description:** Input Edge data can have 'abstract' predicates, when the mode of validation is 'non-strict'.

### info.input_edge.predicate.mixin

**Message:** Input Edge '{edge_id}' has an 'mixin' predicate '{identifier}'.

**Description:** Input Edge data can have 'mixin' predicates, when the mode of validation is 'non-strict'.

### info.query_graph.edge.predicate.abstract

**Message:** Query Graph edge '{edge_id}' has an 'abstract' predicate '{identifier}'.

**Description:** TRAPI Messages in Query Graphs can have 'abstract' predicates, when the mode of validation is 'non-strict'.

### info.query_graph.edge.predicate.mixin

**Message:** Query Graph edge '{edge_id}' has an 'mixin' predicate '{identifier}'.

**Description:** TRAPI Messages in Query Graphs can have 'mixin' predicates, when the mode of validation is 'non-strict'.

### info.knowledge_graph.edge.predicate.abstract

**Message:** Knowledge Graph edge '{edge_id}' has an 'abstract' predicate '{identifier}'.

**Description:** TRAPI Messages in Knowledge Graphs can have 'abstract' predicates, when the mode of validation is 'non-strict'.

### info.knowledge_graph.edge.predicate.mixin

**Message:** Knowledge Graph edge '{edge_id}' has an 'mixin' predicate '{identifier}'.

**Description:** TRAPI Messages in Knowledge Graphs can have 'mixin' predicates, when the mode of validation is 'non-strict'.

### info.knowledge_graph.edge.attribute.type_id.abstract

**Message:** Knowledge Graph edge '{edge_id}' has an 'abstract' attribute_type_id '{identifier}'.

**Description:** TRAPI Messages in Knowledge Graphs can have 'abstract' attribute type identifiers, when the mode of validation is 'non-strict'.

### info.knowledge_graph.edge.attribute.type_id.mixin

**Message:** Knowledge Graph edge '{edge_id}' has an 'mixin' attribute_type_id '{identifier}'.

**Description:** TRAPI Messages in Knowledge Graphs can have 'mixin' attribute type identifiers, when the mode of validation is 'non-strict'.

## Warning

### warning.trapi.response.status.unknown

**Message:** TRAPI Response status code '{identifier}' is unrecognized?

**Description:** The TRAPI Response status code should be one of a standardized set of short codes, e.g. Success, QueryNotTraversable, KPsNotAvailable

### warning.trapi.response.workflow.runner_parameters.null

**Message:** TRAPI Response.workflow.runner_parameters property is missing?

**Description:** If a 'runner_parameters' property value is given for a workflow step specification, it should not be null. This field will be ignored?

### warning.trapi.response.workflow.parameters.null

**Message:** TRAPI Response.workflow.parameters property is missing?

**Description:** If a 'parameters' property value is given for a workflow step specification, it should not be null. This field will be ignored?

### warning.graph.empty

**Message:** {identifier} data is empty?

**Description:** An empty graph in this particular context is allowed but merits a boundary response warning?

### warning.response.knowledge_graph.empty

**Message:** Response returned an empty Message Knowledge Graph?

**Description:** An empty Knowledge Graph is allowed but merits a boundary response warning?

### warning.response.results.empty

**Message:** Response returned empty Message.results?

**Description:** Empty Results is allowed but merits a boundary response warning?

### warning.input_edge.node.category.deprecated

**Message:** Input data node category '{identifier}' is deprecated?

**Description:** Input data node category is deprecated in the current model, to be removed in the future. Review Biolink Model for suitable replacement?

### warning.input_edge.node.id.unmapped_to_category

**Message:** '{identifier}' has identifiers {unmapped_ids} unmapped to the target categories: {categories}?

**Description:** The namespaces of Biolink model node of specified category may be incomplete with respect to identifiers being used in input edge data?

### warning.input_edge.predicate.deprecated

**Message:** Input data edge predicate '{identifier}' is deprecated?

**Description:** Input data edge predicate is deprecated in the current model, to be removed in the future. Review Biolink Model for a suitable replacement?

### warning.input_edge.predicate.non_canonical

**Message:** Input data edge '{identifier}' predicate '{predicate}' is non-canonical?

**Description:** A predicate selected for use as input data should preferably be tagged as 'canonical' in the specified Biolink Model release?

### warning.query_graph.node.category.deprecated

**Message:** Query graph node category '{identifier}' is deprecated?

**Description:** Query graph node category is deprecated in the current model, to be removed in the future. Review Biolink Model for suitable replacement?

### warning.query_graph.node.ids.unmapped_to_categories

**Message:** '{identifier}' has identifiers {unmapped_ids} unmapped to the target categories: {categories}?

**Description:** The namespaces of Biolink model node of specified categories may be incomplete with respect to identifiers being used in the query graph?

### warning.query_graph.edge.predicate.deprecated

**Message:** Query graph edge predicate '{identifier}' is deprecated?

**Description:** Query graph edge predicate is deprecated in the current model, to be removed in the future. Review Biolink Model for a suitable replacement?

### warning.query_graph.edge.predicate.non_canonical

**Message:** Query graph edge '{identifier}' predicate '{predicate}' is non-canonical?

**Description:** A predicate selected for use in a query graph should preferably be tagged as 'canonical' in the specified Biolink Model release?

### warning.knowledge_graph.node.category.deprecated

**Message:** Knowledge graph node category '{identifier}' is deprecated?

**Description:** Knowledge graph node category is deprecated in the current model, to be removed in the future. Review Biolink Model for a suitable replacement?

### warning.knowledge_graph.node.unmapped_prefix

**Message:** '{identifier}' is unmapped to the target categories '{categories}'?

**Description:** ID Namespaces of nodes of specified categories may be incomplete with respect to Biolink Model version being used in the knowledge graph?

### warning.knowledge_graph.node.id.unmapped_to_category

**Message:** {context} node identifier '{identifier}' is unmapped to '{category}'?

**Description:** ID Namespaces of nodes of specified categories may be incomplete with respect to Biolink Model version being used in the knowledge graph?

### warning.knowledge_graph.edge.predicate.deprecated

**Message:** Knowledge graph edge predicate '{identifier}' is deprecated?

**Description:** Knowledge graph edge predicate is deprecated in the current model, to be removed in the future. Review Biolink Model for a suitable replacement?

### warning.knowledge_graph.edge.predicate.non_canonical

**Message:** Knowledge Graph '{identifier}' predicate '{predicate}' is non-canonical?

**Description:** A predicate selected for use in a knowledge graph should preferably be tagged as 'canonical' in the specified Biolink Model release?

### warning.knowledge_graph.edge.qualifiers.empty

**Message:** Edge qualifiers 

**Description:** Knowledge graph edge attributes should record the infores identifier of their knowledge source provenance with respect to ARA.

### warning.knowledge_graph.edge.attribute.type_id.not_association_slot

**Message:** Edge '{edge_id}' attribute_type_id '{identifier}' not an association slot?

**Description:** Knowledge graph edge 'attribute_type_id' value should generally be a term defined within the biolink:association_slot hierarchy.

### warning.knowledge_graph.edge.attribute.type_id.non_biolink_prefix

**Message:** Edge '{identifier}' attribute_type_id '{attribute_type_id}' has a non-Biolink CURIE prefix mapped to Biolink.

**Description:** Non-Biolink CURIEs are tolerated, but not preferred, as term value for the attribute_type_id properties of edge attributes.

### warning.knowledge_graph.edge.attribute.type_id.unknown_prefix

**Message:** Edge '{identifier}' attribute_type_id '{attribute_type_id}' has a CURIE prefix namespace unknown to Biolink!

**Description:** The namespaces of 'attribute_type_id' terms may be incomplete with respect to Biolink Model version being used in the knowledge graph.

### warning.knowledge_graph.edge.attribute.type_id.deprecated

**Message:** Knowledge graph edge attribute '{identifier}' is deprecated?

**Description:** Knowledge graph edge 'attribute_type_id' is deprecated in current model, to be removed in the future. Review Biolink Model for replacement.

### warning.knowledge_graph.edge.provenance.multiple_primary

**Message:** Edge '{identifier}' has recorded multiple 'primary' knowledge sources: '{sources}'?

**Description:** Knowledge graph edge attributes should record only a single primary knowledge source provenance attribute value.

### warning.knowledge_graph.edge.provenance.ara.missing

**Message:** Edge '{identifier}' is missing ARA knowledge source provenance '{ara_source}'?

**Description:** Knowledge graph edge attributes ARAs should record the infores identifier of their knowledge source provenance with respect to ARA.

### warning.knowledge_graph.edge.provenance.kp.missing

**Message:** Edge '{identifier}' attribute values are missing expected Knowledge Provider '{kp_source}' '{kp_source_type}' provenance?

**Description:** Knowledge graph edge attributes of ARAs and KPs should record the infores identifier of their knowledge source provenance with respect to KP.

## Error

### error.non_compliant

**Message:** S-P-O statement '{identifier}' is not compliant to Biolink Model {biolink_release}

**Description:** This knowledge statement is not compliant to the specified release of the Biolink Model. Review associated messages for underlying cause!

### error.trapi.validation

**Message:** TRAPI {identifier} schema exception: '{exception}'!

**Description:** TRAPI query attempt triggered an abnormal server exception as noted.

### error.trapi.request.invalid

**Message:** {identifier} could not generate a valid TRAPI query request object because {reason}!

**Description:** TRAPI query message could not be prepared for the indicated reason, thus query was not attempted.

### error.trapi.response.empty

**Message:** TRAPI Response is missing!

**Description:** TRAPI Response to be validated should not be totally empty but should have a Message body.

### error.trapi.response.unexpected_http_code

**Message:** TRAPI Response has an unexpected HTTP status code: '{status_code}'!

**Description:** TRAPI query attempt returned an abnormal (non-200) server HTTP status code as noted.

### error.trapi.response.message.empty

**Message:** TRAPI Response missing its Message!

**Description:** TRAPI response should at least have non-empty original TRAPI request Message in its reply.

### error.trapi.response.query_graph.missing

**Message:** TRAPI Message is missing its Query Graph!

**Description:** TRAPI response should generally have a TRAPI request message Query Graph key value in its reply.

### error.trapi.response.query_graph.empty

**Message:** Response returned an empty Message Query Graph!

**Description:** TRAPI response should at least have non-empty original TRAPI request message Query Graph in its reply.

### error.trapi.response.knowledge_graph.missing

**Message:** TRAPI Message is missing its Knowledge Graph component!

**Description:** TRAPI response should generally have a TRAPI request message Knowledge Graph key value in its reply.

### error.trapi.response.knowledge_graph.missing_expected_edge

**Message:** TRAPI Response Message is missing an expected edge '{identifier}' in its Knowledge Graph!

**Description:** The given TRAPI Response is expected to return specific edge(s) relating to the original (test edge?) data used to prepare the TRAPI Request!

### error.trapi.response.results.missing

**Message:** TRAPI Message is missing its Results component!

**Description:** TRAPI response should generally have a TRAPI request message Request key value in its reply.

### error.trapi.response.results.non_array

**Message:** Response returned a non-array Message.Results!

**Description:** TRAPI Message.Results must be an array data type (even if empty)

### error.trapi.response.results.missing_bindings

**Message:** Neither the input id '{identifier}' nor resolved aliases were returned in the Result object IDs for node '{output_node_binding}' binding!

**Description:** TRAPI Message.Results cannot resolve its reported identifier mappings to the original query.

### error.input_edge.node.category.missing

**Message:** Input edge node '{identifier}' is missing its category!

**Description:** Category value must be specified in an input test data edge!

### error.input_edge.node.category.not_a_category

**Message:** Input edge node '{identifier}' asserted category '{category}' is not a category term!

**Description:** Category specified in input test data edge node is not recorded as a category term in specified version of Biolink. Replace with a known category!

### error.input_edge.node.category.unknown

**Message:** Input edge node '{node_id}' has unknown category '{identifier}' element!

**Description:** Category specified in input test data edge node is not a model element recorded in specified version of Biolink. Replace with a known category!

### error.input_edge.node.id.missing

**Message:** {identifier} node identifier is missing!

**Description:** Input test data edge data needs to have a specific node identifier for testing!

### error.input_edge.predicate.missing

**Message:** Input test data edge '{identifier}' predicate is missing or empty!

**Description:** Input test edge data needs to have a specific edge predicate for testing!

### error.input_edge.predicate.unknown

**Message:** Input test data edge '{edge_id}' is unknown predicate {identifier}!

**Description:** Predicate specified in input test data edge is not recorded in specified version of Biolink. Replace with a known predicate!

### error.input_edge.predicate.abstract

**Message:** Input Edge '{edge_id}' is not permitted to have an 'abstract' predicate '{identifier}'!

**Description:** Input Edge data validation is currently strict: predicates cannot be 'abstract'! Replace with a concrete predicate.

### error.input_edge.predicate.mixin

**Message:** Input Edge '{edge_id}' is not permitted to have an 'mixin' predicate '{identifier}'!

**Description:** Input Edge data validation is currently strict: predicates cannot be of type 'mixin'! Replace with a concrete predicate.

### error.input_edge.predicate.invalid

**Message:** Edge '{identifier}' predicate '{predicate}' is invalid!

**Description:** Predicate specified in Input Edge is not defined as a predicate in specified version of Biolink. Replace with a proper predicate!

### error.query_graph.node.category.missing

**Message:** Query graph node '{identifier}' is missing its category!

**Description:** Category value must be specified in an query graph edge!

### error.query_graph.node.category.not_a_category

**Message:** Query graph node '{identifier}' asserted category '{category}' is not a category term!

**Description:** Category specified in query graph edge node is not recorded as a category term in specified version of Biolink. Replace with a known category!

### error.query_graph.node.category.unknown

**Message:** Query graph node '{node_id}' has unknown category '{identifier}' element!

**Description:** Category specified in query graph edge node is not a model element recorded in specified version of Biolink. Replace with a known category!

### error.query_graph.node.ids.not_array

**Message:** Node '{identifier}.ids' slot value is not an array!

**Description:** Value of 'ids' slot in Query Graph node must be an array data type (even if empty)!

### error.query_graph.node.categories.not_array

**Message:** Node '{identifier}.categories' slot value is not an array!

**Description:** Value of 'categories' slot in Query Graph node must be an array data type (even if empty)!

### error.query_graph.node.is_set.not_boolean

**Message:** Node '{identifier}.is_set' slot is not a boolean value!

**Description:** The 'is_set' field in node of Query Graph, if present, must be a boolean value!

### error.query_graph.edge.subject.missing

**Message:** Edge '{identifier}' has a missing or empty 'subject' slot value!

**Description:** Query graph edge must have a 'subject' key with a non-empty associated value!

### error.query_graph.edge.subject.missing_from_nodes

**Message:** Edge 'subject' id '{object_id}' is missing from the nodes catalog!

**Description:** Every 'subject' identifier of every edge in a Query Graph must also be recorded in the list of nodes for that graph!

### error.query_graph.edge.object.missing

**Message:** Edge '{identifier}' has a missing or empty 'object' slot value!

**Description:** Query graph edge must have a 'object' key with a non-empty associated value!

### error.query_graph.edge.object.missing_from_nodes

**Message:** Edge 'object' id '{object_id}' is missing from the nodes catalog!

**Description:** Every 'object' identifier of every edge in a Query Graph must also be recorded in the list of nodes for that graph!

### error.query_graph.edge.predicate.missing

**Message:** Edge '{identifier}' predicate is missing or empty!

**Description:** The predicate of Query Graph edge needs to specified using a 'predicate' key with an array list of one or more predicates!

### error.query_graph.edge.predicate.unknown

**Message:** Query graph '{edge_id}' has unknown predicate {identifier}!

**Description:** Predicate specified in Query Graph edge is not defined in specified version of Biolink. Replace with a defined predicate!

### error.query_graph.edge.predicate.not_array

**Message:** Edge '{identifier}' predicate slot value is not an array!

**Description:** Value of 'predicate' slot value in Query Graph must be an array data type!

### error.query_graph.edge.predicate.empty_array

**Message:** Edge '{identifier}' predicate slot value is an empty array!

**Description:** Value of 'predicate' array slot value in Query Graph must contain one or more predicates!

### error.query_graph.edge.predicate.abstract

**Message:** Query Graph edge '{edge_id}' is not permitted to have an 'abstract' predicate '{identifier}'!

**Description:** Query Graph data validation is currently strict: cannot have 'abstract' predicates! Replace with a concrete predicate.

### error.query_graph.edge.predicate.mixin

**Message:** Query Graph edge '{edge_id}' is not permitted to have an 'mixin' predicate '{identifier}'!

**Description:** Query Graph data validation is currently strict: cannot have 'mixin' predicates! Replace with a concrete predicate.

### error.query_graph.edge.predicate.invalid

**Message:** Edge '{identifier}' predicate '{predicate}' is invalid!

**Description:** Predicate specified in Query Graph edge is not defined as a predicate in specified version of Biolink. Replace with a proper predicate!

### error.query_graph.edge.attribute_constraints.not_array

**Message:** Edge '{identifier}' attribute_constraints property value is not an array!

**Description:** Value of 'attribute_constraints' slot value in a Query Graph must be an array data type!

### error.query_graph.edge.qualifier_constraints.qualifier_set.empty

**Message:** Edge '{identifier}' qualifier_set property value is empty!

**Description:** Value of a 'qualifier_constraints.qualifier_set' property in a Query Graph must not be non-empty array!

### error.query_graph.edge.qualifier_constraints.qualifier_set.qualifier.type_id.unknown

**Message:** Edge '{edge_id}' qualifier type_id '{identifier}' is unknown!

**Description:** A qualifier qualifier_type_id must be defined in the specified version of Biolink!

### error.query_graph.edge.qualifier_constraints.qualifier_set.qualifier.value.unresolved

**Message:** Edge '{identifier}' qualifier_value '{qualifier_value}' for '{qualifier_type_id}' cannot be resolved!

**Description:** A 'qualifier_value' for the specified 'qualifier_type_id' of a qualifier likely could not be resolved without knowledge of the edge category!

### error.knowledge_graph.nodes.empty

**Message:** No nodes found!

**Description:** Knowledge graph in TRAPI messages must have a 'nodes' key and non-empty associated value!

### error.knowledge_graph.edges.empty

**Message:** No edges found!

**Description:** Knowledge graph in TRAPI messages must have a 'edges' key and non-empty associated value!

### error.knowledge_graph.node.category.missing

**Message:** Input edge node '{identifier}' is missing its category!

**Description:** Category value must be specified in an knowledge graph edge!

### error.knowledge_graph.node.category.not_a_category

**Message:** Input edge node '{identifier}' asserted category '{category}' is not a category term!

**Description:** Category specified in knowledge graph edge node is not recorded as a category term in specified version of Biolink. Replace with a known category!

### error.knowledge_graph.node.category.unknown

**Message:** Input edge node '{node_id}' has unknown category '{identifier}' element!

**Description:** Category specified in knowledge graph edge node is not a model element recorded in specified version of Biolink. Replace with a known category!

### error.knowledge_graph.node.id.missing

**Message:** {identifier} node identifier is missing!

**Description:** Knowledge graph node must have a 'id' key with a non-empty associated value!

### error.knowledge_graph.node.missing_categories

**Message:** Node '{identifier}' is missing its categories!

**Description:** Knowledge graph node must have a 'categories' key with a non-empty associated value!

### error.knowledge_graph.node.ids.not_array

**Message:** Node '{identifier}.ids' slot value is not an array!

**Description:** Value of 'ids' slot in Query Graph node must be an array data type!

### error.knowledge_graph.node.empty_ids

**Message:** Node '{identifier}.ids' slot array is empty!

**Description:** Value of 'ids' array slot in Knowledge Graph node must contain one or more node identifiers!

### error.knowledge_graph.node.categories.not_array

**Message:** Node '{identifier}.categories' slot value is not an array!

**Description:** Value of 'categories' slot in Knowledge Graph node must be an array data type!

### error.knowledge_graph.node.empty_categories

**Message:** Node '{identifier}.categories' slot array is empty!

**Description:** Value of 'categories' array slot in Knowledge Graph node must contain one or more node category terms!

### error.knowledge_graph.node.is_set.not_boolean

**Message:** Node '{identifier}.is_set' slot is not a boolean value!

**Description:** The 'is_set' field in node of Knowledge Graph, if present, must be a boolean value!

### error.knowledge_graph.edge.subject.missing

**Message:** Edge '{identifier}' has a missing or empty 'subject' slot value!

**Description:** Knowledge graph edge must have a 'subject' key with a non-empty associated value!

### error.knowledge_graph.edge.subject.missing_from_nodes

**Message:** Edge 'subject' id '{object_id}' is missing from the nodes catalog!

**Description:** Every 'subject' identifier of every edge in a Knowledge Graph must also be recorded in the list of nodes for that graph!

### error.knowledge_graph.edge.object.missing

**Message:** Edge '{identifier}' has a missing or empty 'object' slot value!

**Description:** Knowledge graph edge must have a 'object' key with a non-empty associated value!

### error.knowledge_graph.edge.object.missing_from_nodes

**Message:** Edge 'object' id '{object_id}' is missing from the nodes catalog!

**Description:** Every 'object' identifier of every edge in a Knowledge Graph must also be recorded in the list of nodes for that graph!

### error.knowledge_graph.edge.predicate.missing

**Message:** Edge '{identifier}' predicate is missing or empty!

**Description:** Knowledge graph edge must have a 'predicate' key with a non-empty associated value!

### error.knowledge_graph.edge.predicate.unknown

**Message:** Knowledge graph '{edge_id}' has unknown predicate {identifier}!

**Description:** Predicate specified in Knowledge Graph edge is not defined in specified version of Biolink. Replace with a defined predicate!

### error.knowledge_graph.edge.predicate.invalid

**Message:** Edge '{identifier}' predicate '{predicate}' is invalid!

**Description:** Predicate specified in Knowledge Graph edge is not defined as a predicate in specified version of Biolink. Replace with a defined predicate!

### error.knowledge_graph.edge.predicate.not_array

**Message:** Edge '{identifier}' predicate slot value is not an array!

**Description:** Value of the 'predicate' slot in Knowledge Graph edge must be an array data type!

### error.knowledge_graph.edge.predicate.empty_array

**Message:** Value of the 'predicate' array slot in Knowledge Graph edge must contain one or more predicates!

**Description:** Value of the 'predicate' array slot in Knowledge Graph edge must contain one or more predicates!

### error.knowledge_graph.edge.predicate.abstract

**Message:** Knowledge Graph edge '{edge_id}' is not permitted to have an 'abstract' predicate '{identifier}'!

**Description:** Knowledge Graph data validation is currently strict: cannot have 'abstract' predicates! Replace with a concrete predicate.

### error.knowledge_graph.edge.predicate.mixin

**Message:** Knowledge Graph edge '{edge_id}' is not permitted to have an 'mixin' predicate '{identifier}'!

**Description:** Knowledge Graph data validation is currently strict: cannot have 'mixin' predicates! Replace with a concrete predicate.

### error.knowledge_graph.edge.attribute.missing

**Message:** Edge '{identifier}' has no 'attributes' key!

**Description:** Knowledge graph edge must have a 'attributes' key with a non-empty associated value!

### error.knowledge_graph.edge.attribute.empty

**Message:** Edge '{identifier}' has empty attributes!

**Description:** Value of 'attributes' slot in Knowledge Graph edge must contain a list of one or more attributes!

### error.knowledge_graph.edge.attribute.not_array

**Message:** Edge '{identifier}' attributes are not an array!

**Description:** Value of the 'attributes' slot in Knowledge Graph edge must be an array of attributes!

### error.knowledge_graph.edge.attribute.type_id.unknown

**Message:** Knowledge graph '{edge_id}' has unknown attribute_type_id {identifier}!

**Description:** Edge Attribute type identifier specified in knowledge graph edge is not recorded in specified version of Biolink. Replace with a known term!

### error.knowledge_graph.edge.attribute.type_id.abstract

**Message:** Knowledge Graph edge '{edge_id}' is not permitted to have an 'abstract' attribute_type_id '{identifier}'!

**Description:** Edge data validation is currently strict: attribute type identifiers cannot be 'abstract'. Replace with a concrete attribute_type_id!

### error.knowledge_graph.edge.attribute.type_id.mixin

**Message:** Knowledge Graph edge '{edge_id}' is not permitted to have an 'mixin' attribute_type_id '{identifier}'!

**Description:** Edge data validation is currently strict: attribute type identifiers cannot be of type 'mixin'. Replace with a concrete attribute_type_id!

### error.knowledge_graph.edge.attribute.type_id.missing

**Message:** Edge '{identifier}' attribute is missing its 'attribute_type_id' property!

**Description:** The attribute of a Knowledge graph edge must have a 'attribute_type_id' key with a non-empty associated value!

### error.knowledge_graph.edge.attribute.type_id.empty

**Message:** Edge'{identifier}' attribute empty 'attribute_type_id' property!

**Description:** The value of the 'attribute_type_id' of an attribute of a Knowledge graph edge must not be empty!

### error.knowledge_graph.edge.attribute.type_id.not_curie

**Message:** Edge '{identifier}' attribute_type_id '{attribute_type_id}' is not a CURIE!

**Description:** The 'attribute_type_id' of a Knowledge graph edge attribute must be a controlled vocabulary term specified by a CURIE!

### error.knowledge_graph.edge.attribute.value.missing

**Message:** Edge '{identifier}' attribute is missing its 'value' property!

**Description:** An attribute of a Knowledge graph edge must have a 'value' key with a non-empty associated value!

### error.knowledge_graph.edge.attribute.value.empty

**Message:** Edge '{identifier}' attribute empty 'value' property!

**Description:** The value of an attribute of a Knowledge graph edge must not be empty!

### error.knowledge_graph.edge.provenance.infores.missing

**Message:** Edge '{identifier}' has provenance value '{infores}' which is not a well-formed InfoRes CURIE!

**Description:** The value of an attribute specifying the provenance of a Knowledge graph edge must be the well-formed InfoRes CURIE of a knowledge source!

### error.knowledge_graph.edge.provenance.missing_primary

**Message:** Edge '{identifier}' does not record its 'primary' knowledge source?

**Description:** Knowledge graph edge attributes should record the 'infores' identifier of their primary knowledge source provenance with respect to KP.

### error.knowledge_graph.edge.qualifiers.not_array

**Message:** Edge '{identifier}' 'qualifiers' are not an array!

**Description:** Value of the 'qualifiers' slot in Knowledge Graph edge must be an array of attributes!

### error.knowledge_graph.edge.qualifiers.empty

**Message:** Edge '{identifier}' qualifiers property value is empty!

**Description:** Value of a 'qualifiers' property in a Knowledge Graph must not be non-empty array!

### error.knowledge_graph.edge.qualifiers.qualifier.type_id.unknown

**Message:** Edge '{edge_id}' qualifier type_id '{identifier}' is unknown!

**Description:** A qualifier qualifier_type_id must be defined in the specified version of Biolink!

### error.knowledge_graph.edge.qualifiers.qualifier.value.unresolved

**Message:** Edge '{identifier}' qualifier_value '{qualifier_value}' for '{qualifier_type_id}' cannot be resolved!

**Description:** A 'qualifier_value' for the specified 'qualifier_type_id' of a qualifier likely could not be resolved without knowledge of the edge category!

