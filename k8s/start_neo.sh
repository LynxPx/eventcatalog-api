#!/bin/bash
term_width=$(tput cols)
msg="Exposing Local Neo4j DB Service for connecton..."
padding=$(( (term_width - ${#message}) / 2 -10))

echo ""
line=$(printf '%*s' "$term_width" | tr ' ' '#')
echo "$line"
printf "%*s\n" $((padding + ${#msg})) "$msg"
echo "$line"
echo ""


kubectl apply -f neo4j-service.yaml
minikube service neo4j-service -n catalog