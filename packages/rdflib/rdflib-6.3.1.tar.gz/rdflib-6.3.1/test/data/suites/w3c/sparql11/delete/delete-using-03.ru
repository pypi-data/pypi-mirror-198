PREFIX     : <http://example.org/> 
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 

DELETE 
{
  ?s ?p ?o .
}
USING <http://example.org/g2>
WHERE 
{
  ?s foaf:knows :d .
  ?s ?p ?o 
}
