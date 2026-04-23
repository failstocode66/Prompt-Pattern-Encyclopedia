# Prompt-Pattern-Encyclopedia

A structured, testable, and evolving system for prompt engineering.

## Purpose

This repository is a living system for:

* Designing reusable prompt patterns
* Evaluating prompt reliability and performance
* Composing patterns into higher-level systems
* Tracking prompt evolution over time

## Structure

* /patterns/core → Stable, validated patterns
* /patterns/lab → Experimental and in-progress patterns
* /compositions → Multi-pattern systems
* /evals → Test cases and evaluation logic
* /docs → Supporting documentation

## Pattern Lifecycle

IDEA → /lab → tested → scored → promoted → /core → revalidated → updated

## Promotion Criteria (Lab → Core)

A pattern must:

* Pass defined test cases
* Produce consistent outputs (low variance)
* Include at least 2 real-use examples
* Document known failure modes
* Meet scoring threshold (≥ 12/15)

## Validation Principle: Basline Comparison

All patterns must demonstrate a measureable or observable improvement over a baseline(no-pattern) prompt.

This means:

* A patternshould produce notably better results than a raw prompt
* Improvements may include accuracy, structure, consistency, or clarity
* Patterns that do not show a clear delta should remain in /lab or be rejected

Whenever possible, patterns should include a baseline vs. pattern comparison to make this improvement explicit 

## Scoring System

Each pattern is evaluated on:

* Clarity (1–5)
* Consistency (1–5)
* Reusability (1–5)

## Design Principles

* Composability over cleverness
* Explicit constraints over vague instructions
* Testability over intuition
* Failure-aware design

## Status

This is an evolving system. Patterns are continuously tested, refined, and revalidated.
