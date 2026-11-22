"""bilingual curriculum content

Adds the English half of the curriculum and the per-chapter resources the new learning
page needs: category grouping, enrichment flag, interactive visualization keys, revision
notes and video recommendations.

Revision ID: b1c2d3e4f5a6
Revises: 8783068a8be1
Create Date: 2026-11-22 10:05:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1c2d3e4f5a6'
down_revision: Union[str, None] = '8783068a8be1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ---- chapters: bilingual summary, category, enrichment flag and resources ----
    with op.batch_alter_table('chapters') as batch_op:
        batch_op.add_column(
            sa.Column('summary_en', sa.Text(), nullable=True)
        )
        batch_op.add_column(
            sa.Column(
                'category',
                sa.String(length=20),
                nullable=False,
                server_default=sa.text("'biology'"),
            )
        )
        batch_op.add_column(
            sa.Column(
                'is_enrichment',
                sa.Boolean(),
                nullable=False,
                server_default=sa.text('0'),
            )
        )
        batch_op.add_column(
            sa.Column('visualizations', sa.JSON(), nullable=False, server_default=sa.text("'[]'"))
        )
        batch_op.add_column(
            sa.Column('notes_kn', sa.JSON(), nullable=False, server_default=sa.text("'[]'"))
        )
        batch_op.add_column(
            sa.Column('notes_en', sa.JSON(), nullable=False, server_default=sa.text("'[]'"))
        )
        batch_op.add_column(
            sa.Column('videos', sa.JSON(), nullable=False, server_default=sa.text("'[]'"))
        )

    # ---- lessons: English explanation and example ----
    with op.batch_alter_table('lessons') as batch_op:
        batch_op.add_column(sa.Column('body_en', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('example_en', sa.Text(), nullable=True))

    # ---- learning objectives: English wording ----
    with op.batch_alter_table('learning_objectives') as batch_op:
        batch_op.add_column(sa.Column('text_en', sa.Text(), nullable=True))

    # ---- practice questions: English question, options and explanation ----
    with op.batch_alter_table('practice_questions') as batch_op:
        batch_op.add_column(sa.Column('question_en', sa.Text(), nullable=True))
        batch_op.add_column(
            sa.Column('options_en', sa.JSON(), nullable=False, server_default=sa.text("'[]'"))
        )
        batch_op.add_column(sa.Column('explanation_en', sa.Text(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('practice_questions') as batch_op:
        batch_op.drop_column('explanation_en')
        batch_op.drop_column('options_en')
        batch_op.drop_column('question_en')

    with op.batch_alter_table('learning_objectives') as batch_op:
        batch_op.drop_column('text_en')

    with op.batch_alter_table('lessons') as batch_op:
        batch_op.drop_column('example_en')
        batch_op.drop_column('body_en')

    with op.batch_alter_table('chapters') as batch_op:
        batch_op.drop_column('videos')
        batch_op.drop_column('notes_en')
        batch_op.drop_column('notes_kn')
        batch_op.drop_column('visualizations')
        batch_op.drop_column('is_enrichment')
        batch_op.drop_column('category')
        batch_op.drop_column('summary_en')
